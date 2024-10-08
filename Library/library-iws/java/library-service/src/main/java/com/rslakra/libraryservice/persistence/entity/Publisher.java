package com.rslakra.libraryservice.persistence.entity;

import com.rslakra.appsuite.core.ToString;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Table;

/**
 * @author Rohtash Lakra
 * @created 10/9/21 3:56 PM
 */
@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(name = "publishers")
public class Publisher extends Person {

    /**
     * Returns the string representation of this object.
     *
     * @return
     */
    @Override
    public String toString() {
        return ToString.of(Publisher.class)
            .add("email", getEmail())
            .add("firstName", getFirstName())
            .add("middleName", getMiddleName())
            .add("lastName", getLastName())
            .toString();
    }

}
