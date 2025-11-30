package com.rslakra.libraryservice.persistence.entity;

import com.rslakra.appsuite.core.ToString;
import com.rslakra.appsuite.spring.persistence.entity.NamedEntity;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

/**
 * <pre>
 *  {
 *   "title": "Moby Dick",
 *   "author": "Herman Melville",
 *   "body": "Some years ago ...",
 *   "isbn": "1111979723",
 *   "copiesOwned": 3
 *  }
 * </pre>
 *
 * @author Rohtash Lakra
 * @created 10/9/21 3:56 PM
 */
@Getter
@Setter
@NoArgsConstructor
@Entity
//@EntityListeners(BaseEntityListener.class)
@Table(name = "books")
public class Book extends NamedEntity<Long> {

    @Column(name = "title", length = 64, nullable = false)
    private String title;

    public String author;
    public String content;
    public String isbn;

    @Column(name = "published_on", nullable = false, updatable = false)
    private Long publishedOn;

    /**
     * Returns the string representation of this object.
     *
     * @return
     */
    @Override
    public String toString() {
        return ToString.of(Book.class)
            .add("name", getName())
            .toString();
    }

}
