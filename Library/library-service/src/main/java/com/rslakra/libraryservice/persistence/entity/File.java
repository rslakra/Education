package com.rslakra.libraryservice.persistence.entity;

import com.rslakra.appsuite.core.ToString;
import com.rslakra.appsuite.spring.persistence.entity.NamedEntity;
import com.rslakra.libraryservice.enums.EntityStatus;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

/**
 * @author Rohtash Lakra
 * @created 8/4/21 5:59 PM
 */
@Getter
@Setter
@Entity
@EntityListeners(FileEntityListener.class)
@Table(name = "files")
public class File extends NamedEntity<Long> {
    
    @Column(name = "status")
    @Enumerated(value = EnumType.STRING)
    private EntityStatus status = EntityStatus.DISABLED;
    
    @Column(name = "contents")
    private String contents;
    
    public File() {
        super();
    }
    
    /**
     * @param name
     * @param contents
     */
    public File(String name, String contents) {
        super(name);
        this.contents = contents;
    }
    
    /**
     * Returns the string representation of this object.
     *
     * @return
     */
    @Override
    public String toString() {
        return ToString.of(File.class)
                .add("name", getName())
                .add("status", getStatus())
                .add("contents", getContents())
                .toString();
    }
}
