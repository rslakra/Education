package com.rslakra.libraryclient.config;

import com.rslakra.libraryclient.service.RestService;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.client.ClientHttpRequestInterceptor;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.util.DefaultUriBuilderFactory;

import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Collections;

/**
 * REST Service configuration for Spring Boot 3.x
 *
 * @author Rohtash Lakra
 * @created 10/9/21 4:52 PM
 */
@Configuration
@PropertySource("classpath:application.properties")
public class RestServiceConfig {

    @Autowired
    private CloseableHttpClient httpClient;

    @Value("${apiHostBaseUrl}")
    private String apiHostBaseUrl;

    @Value("${libraryService.username:admin}")
    private String username;

    @Value("${libraryService.password:Admin123}")
    private String password;

    /**
     * Creates the RestService bean with Basic Auth interceptor.
     *
     * @return RestService
     */
    @Bean
    public RestService restService() {
        final RestService restService = new RestService(apiHostBaseUrl, clientHttpRequestFactory());
        restService.setUriTemplateHandler(new DefaultUriBuilderFactory(apiHostBaseUrl));
        
        // Add Basic Auth interceptor
        restService.setInterceptors(Collections.singletonList(basicAuthInterceptor()));
        
        return restService;
    }

    /**
     * Creates a Basic Auth interceptor for REST API calls.
     *
     * @return ClientHttpRequestInterceptor
     */
    private ClientHttpRequestInterceptor basicAuthInterceptor() {
        return (request, body, execution) -> {
            String auth = username + ":" + password;
            String encodedAuth = Base64.getEncoder().encodeToString(auth.getBytes(StandardCharsets.UTF_8));
            request.getHeaders().add(HttpHeaders.AUTHORIZATION, "Basic " + encodedAuth);
            return execution.execute(request, body);
        };
    }

    /**
     * Creates the HttpComponentsClientHttpRequestFactory bean.
     *
     * @return HttpComponentsClientHttpRequestFactory
     */
    @Bean
    @ConditionalOnMissingBean
    public HttpComponentsClientHttpRequestFactory clientHttpRequestFactory() {
        HttpComponentsClientHttpRequestFactory clientHttpRequestFactory = new HttpComponentsClientHttpRequestFactory();
        clientHttpRequestFactory.setHttpClient(httpClient);
        return clientHttpRequestFactory;
    }
}
