package com.rslakra.libraryclient.config;

import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.config.ConnectionConfig;
import org.apache.hc.client5.http.config.RequestConfig;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.client5.http.impl.io.PoolingHttpClientConnectionManager;
import org.apache.hc.client5.http.impl.io.PoolingHttpClientConnectionManagerBuilder;
import org.apache.hc.client5.http.ssl.SSLConnectionSocketFactoryBuilder;
import org.apache.hc.client5.http.ssl.TrustSelfSignedStrategy;
import org.apache.hc.core5.http.io.SocketConfig;
import org.apache.hc.core5.pool.PoolConcurrencyPolicy;
import org.apache.hc.core5.pool.PoolReusePolicy;
import org.apache.hc.core5.ssl.SSLContextBuilder;
import org.apache.hc.core5.util.TimeValue;
import org.apache.hc.core5.util.Timeout;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.Scheduled;

import java.security.KeyManagementException;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.util.concurrent.TimeUnit;

/**
 * HTTP Client configuration for Apache HttpClient 5.x (Spring Boot 3.x compatible)
 *
 * @author Rohtash Lakra
 * @created 10/9/21 4:51 PM
 */
@Configuration
public class HttpClientConfig {

    private static final Logger LOGGER = LoggerFactory.getLogger(HttpClientConfig.class);

    //@formatter:off
    private static final int CONNECT_TIMEOUT = Integer.getInteger("HTTP_CONNECT_TIMEOUT", 10_000);
    private static final int REQUEST_TIMEOUT = Integer.getInteger("HTTP_REQUEST_TIMEOUT", 30_000);
    private static final int SOCKET_TIMEOUT = Integer.getInteger("HTTP_SOCKET_TIMEOUT", REQUEST_TIMEOUT);
    private static final int MAX_TOTAL_CONNECTIONS = Integer.getInteger("MAX_TOTAL_CONNECTIONS", 50);
    private static final int DEFAULT_KEEP_ALIVE_TIME_MILLIS = Integer.getInteger("DEFAULT_KEEP_ALIVE_TIME_MILLIS", 20_000);
    private static final int CLOSE_IDLE_CONNECTION_WAIT_TIME_SECS = Integer.getInteger("CLOSE_IDLE_CONNECTION_WAIT_TIME_SECS", 30);
    //@formatter:on

    /**
     * Creates a PoolingHttpClientConnectionManager with SSL support.
     *
     * @return PoolingHttpClientConnectionManager
     */
    @Bean
    public PoolingHttpClientConnectionManager poolingConnectionManager() {
        try {
            return PoolingHttpClientConnectionManagerBuilder.create()
                .setSSLSocketFactory(SSLConnectionSocketFactoryBuilder.create()
                    .setSslContext(SSLContextBuilder.create()
                        .loadTrustMaterial(null, new TrustSelfSignedStrategy())
                        .build())
                    .build())
                .setDefaultSocketConfig(SocketConfig.custom()
                    .setSoTimeout(Timeout.ofMilliseconds(SOCKET_TIMEOUT))
                    .build())
                .setDefaultConnectionConfig(ConnectionConfig.custom()
                    .setConnectTimeout(Timeout.ofMilliseconds(CONNECT_TIMEOUT))
                    .setSocketTimeout(Timeout.ofMilliseconds(SOCKET_TIMEOUT))
                    .setTimeToLive(TimeValue.ofMilliseconds(DEFAULT_KEEP_ALIVE_TIME_MILLIS))
                    .build())
                .setPoolConcurrencyPolicy(PoolConcurrencyPolicy.STRICT)
                .setConnPoolPolicy(PoolReusePolicy.LIFO)
                .setMaxConnTotal(MAX_TOTAL_CONNECTIONS)
                .setMaxConnPerRoute(MAX_TOTAL_CONNECTIONS / 2)
                .build();
        } catch (NoSuchAlgorithmException | KeyStoreException | KeyManagementException e) {
            LOGGER.error("Pooling Connection Manager initialization failure: {}", e.getMessage(), e);
            // Return a basic connection manager without SSL customization
            return PoolingHttpClientConnectionManagerBuilder.create()
                .setMaxConnTotal(MAX_TOTAL_CONNECTIONS)
                .setMaxConnPerRoute(MAX_TOTAL_CONNECTIONS / 2)
                .build();
        }
    }

    /**
     * Creates a CloseableHttpClient with connection pooling.
     *
     * @return CloseableHttpClient
     */
    @Bean
    public CloseableHttpClient httpClient() {
        RequestConfig requestConfig = RequestConfig.custom()
            .setConnectionRequestTimeout(Timeout.ofMilliseconds(REQUEST_TIMEOUT))
            .setResponseTimeout(Timeout.ofMilliseconds(REQUEST_TIMEOUT))
            .build();

        return HttpClients.custom()
            .setDefaultRequestConfig(requestConfig)
            .setConnectionManager(poolingConnectionManager())
            .evictExpiredConnections()
            .evictIdleConnections(TimeValue.ofSeconds(CLOSE_IDLE_CONNECTION_WAIT_TIME_SECS))
            .build();
    }

    /**
     * Monitors and closes idle/expired connections.
     *
     * @param connectionManager the connection manager to monitor
     * @return Runnable for scheduled execution
     */
    @Bean
    public Runnable idleConnectionMonitor(final PoolingHttpClientConnectionManager connectionManager) {
        return new Runnable() {

            @Override
            @Scheduled(fixedDelay = 10000)
            public void run() {
                try {
                    if (connectionManager != null) {
                        LOGGER.trace("IdleConnectionMonitor - Closing expired and idle connections...");
                        connectionManager.closeExpired();
                        connectionManager.closeIdle(TimeValue.ofSeconds(CLOSE_IDLE_CONNECTION_WAIT_TIME_SECS));
                    } else {
                        LOGGER.trace("IdleConnectionMonitor - Connection manager is not initialized");
                    }
                } catch (Exception e) {
                    LOGGER.error("IdleConnectionMonitor - Exception occurred: {}", e.getMessage(), e);
                }
            }
        };
    }
}
