package com.rslakra.libraryservice.persistence.entity;

import com.rslakra.appsuite.core.BeanUtils;
import com.rslakra.appsuite.core.ToString;
import com.rslakra.libraryservice.enums.EntityStatus;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.CreatedDate;

import javax.persistence.*;
import java.util.Collections;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

/**
 * @author Rohtash Lakra
 * @created 8/20/21 7:14 PM
 */
@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(name = "users")
public class User extends Person {
    
    @Column(name = "user_name", unique = true, updatable = false, nullable = false)
    private String userName;
    
    @Column(name = "status", nullable = false)
    @Enumerated(value = EnumType.STRING)
    private EntityStatus status = EntityStatus.DISABLED;
    
    @Column(name = "test_user")
    private Boolean testUser = Boolean.FALSE;
    
    @Column(name = "registered_on", nullable = false, updatable = false)
    @CreatedDate
    @Temporal(TemporalType.TIMESTAMP)
    private Date registeredOn;
    
    @Column(name = "country_code")
    private String countryCode;
    
    @Column(name = "phone_number")
    private String phoneNumber;
    
    @Column(name = "dob")
    private Date dob;
    
    @Column(name = "social_identity")
    private String socialIdentity;
    
    @Column(name = "profile_urls")
    private String profileUrls;
    
    @Column(name = "referral_code")
    private String referralCode;
    
    @Column(name = "metadata")
    private String metadata;
    
    @ManyToMany(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JoinTable(name = "users_roles", joinColumns = @JoinColumn(name = "user_id"), inverseJoinColumns = @JoinColumn(name = "role_id"))
    private Set<Role> roles = new HashSet<>();
    
    /**
     * Adds the <code>Set<Role></code>.
     *
     * @param userRoles
     */
    public void addRoles(final Set<Role> userRoles) {
        if (BeanUtils.isNotEmpty(userRoles)) {
            getRoles().addAll(userRoles);
        }
    }
    
    /**
     * @param userRoles
     * @return
     */
    public boolean hasRoles(final Set<Role> userRoles) {
        /*
         * The Collections.disjoint(A, B) returns true if the two specified collections have no elements in common
         * otherwise returns false if the collections contains any common elements.
         */
        return ((BeanUtils.isNotEmpty(getRoles()) && BeanUtils.isNotEmpty(userRoles)) && Collections.disjoint(
                getRoles(), userRoles));
    }
    
    /**
     * Returns the string representation of this object.
     *
     * @return
     */
    @Override
    public String toString() {
        return ToString.of(User.class)
                .add("userName", getUserName())
                .add("email", getEmail())
                .add("firstName", getFirstName())
                .add("middleName", getMiddleName())
                .add("lastName", getLastName())
                .add("status", getStatus())
                .add("testUser", getTestUser())
                .add("registeredOn", getRegisteredOn())
                .add("countryCode", getCountryCode())
                .add("phoneNumber", getPhoneNumber())
                .add("dob", getDob())
                .add("socialIdentity", getSocialIdentity())
                .add("profileUrls", getProfileUrls())
                .add("referralCode", getReferralCode())
                .add("metadata", getMetadata())
                .add("roles", getRoles())
                .toString();
    }
}
