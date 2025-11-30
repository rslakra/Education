package com.rslakra.libraryservice.persistence.entity;

import com.rslakra.appsuite.core.ToString;
import com.rslakra.appsuite.spring.persistence.entity.AbstractEntity;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import jakarta.persistence.Entity;
import jakarta.persistence.EntityListeners;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.ForeignKey;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

/**
 * @author Rohtash Lakra
 * @created 8/4/21 6:03 PM
 */
@Getter
@Setter
@NoArgsConstructor
@Entity
@EntityListeners(AuditingEntityListener.class)
@Table(name = "file_history")
public class FileHistory extends AbstractEntity<Long> {

    private String contents;

    @Enumerated(EnumType.STRING)
    private Operation operation;

    @ManyToOne
    @JoinColumn(name = "file_id", foreignKey = @ForeignKey(name = "FK_FileHistory_File"))
    private File file;

    /**
     * @param file
     * @param operation
     */
    public FileHistory(File file, Operation operation) {
        if (file != null) {
            this.file = file;
            this.contents = file.getContents();
        }

        this.operation = operation;
    }

    /**
     * Returns the string representation of this object.
     *
     * @return
     */
    @Override
    public String toString() {
        return ToString.of(FileHistory.class)
            .add("contents=" + getContents())
            .add("operation=" + getOperation())
            .add("file=" + getFile())
            .toString();
    }
}
