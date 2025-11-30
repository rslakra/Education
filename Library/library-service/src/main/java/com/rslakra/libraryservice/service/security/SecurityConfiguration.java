package com.rslakra.libraryservice.service.security;

import org.springframework.boot.autoconfigure.security.servlet.PathRequest;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;

/**
 * Security configuration for Spring Boot 3.x
 *
 * @author Rohtash Lakra
 * @created 8/20/21 5:08 PM
 */
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    /**
     * Main security filter chain for the application.
     *
     * @param http HttpSecurity
     * @return SecurityFilterChain
     * @throws Exception if configuration fails
     */
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                // Allow H2 console
                .requestMatchers(AntPathRequestMatcher.antMatcher("/h2/**")).permitAll()
                // Allow public resources
                .requestMatchers("/", "/index", "/about", "/contact", "/services", "/clients").permitAll()
                .requestMatchers("/css/**", "/js/**", "/images/**", "/webjars/**").permitAll()
                .requestMatchers("/api-docs/**", "/v3/api-docs/**", "/swagger-ui/**", "/swagger-ui.html", "/swagger-resources/**").permitAll()
                .requestMatchers("/error").permitAll()
                // Allow static resources
                .requestMatchers(PathRequest.toStaticResources().atCommonLocations()).permitAll()
                // Require authentication for everything else
                .anyRequest().authenticated()
            )
            // Disable CSRF for H2 console (it doesn't support CSRF tokens)
            .csrf(csrf -> csrf
                .ignoringRequestMatchers(PathRequest.toH2Console())
            )
            // Allow frames from same origin for H2 console (it uses iframes)
            .headers(headers -> headers
                .frameOptions(frame -> frame.sameOrigin())
            )
            .formLogin(form -> form
                .loginPage("/login")
                .permitAll()
            )
            .logout(logout -> logout.permitAll());

        return http.build();
    }
}
