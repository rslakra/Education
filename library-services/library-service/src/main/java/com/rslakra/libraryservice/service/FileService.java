package com.rslakra.libraryservice.service;

import com.devamatre.appsuite.spring.service.AbstractService;
import com.rslakra.libraryservice.persistence.entity.File;

import java.util.List;

/**
 * @author Rohtash Lakra
 * @created 8/20/21 8:11 PM
 */
public interface FileService extends AbstractService<File, Long> {

    /**
     * Returns the list of files by name.
     *
     * @param name
     * @return
     */
    public File getByName(String name);

    /**
     * Returns the list of files by contents.
     *
     * @param contents
     * @return
     */
    public List<File> getByContents(String contents);

}
