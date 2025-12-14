package com.rslakra.libraryservice.service.impl;

import com.rslakra.appsuite.core.BeanUtils;
import com.rslakra.appsuite.spring.exception.DuplicateRecordException;
import com.rslakra.appsuite.spring.exception.InvalidRequestException;
import com.rslakra.appsuite.spring.exception.NoRecordFoundException;
import com.rslakra.appsuite.spring.filter.Filter;
import com.rslakra.appsuite.spring.persistence.ServiceOperation;
import com.rslakra.appsuite.spring.service.AbstractServiceImpl;
import com.rslakra.libraryservice.persistence.entity.File;
import com.rslakra.libraryservice.persistence.entity.FileHistory;
import com.rslakra.libraryservice.persistence.repository.FileHistoryRepository;
import com.rslakra.libraryservice.persistence.repository.FileRepository;
import com.rslakra.libraryservice.service.FileService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 * @author Rohtash Lakra
 * @created 10/9/21 5:50 PM
 */
@Service
public class FileServiceImpl extends AbstractServiceImpl<File, Long> implements FileService {

    // LOGGER
    private static final Logger LOGGER = LoggerFactory.getLogger(FileServiceImpl.class);

    // fileRepository
    private final FileRepository fileRepository;
    private final FileHistoryRepository fileHistoryRepository;

    /**
     * @param fileRepository
     * @param fileHistoryRepository
     */
    @Autowired
    public FileServiceImpl(final FileRepository fileRepository, final FileHistoryRepository fileHistoryRepository) {
        this.fileRepository = fileRepository;
        this.fileHistoryRepository = fileHistoryRepository;
    }

    /**
     * Returns the list of all <code>T</code> objects.
     *
     * @return
     */
    @Override
    public List<File> getAll() {
        final List<File> files = fileRepository.findAll();
        LOGGER.debug("getAllObjects(), files:{}", files);
        return files;
    }

    /**
     * @param id
     * @return
     */
    @Override
    public File getById(Long id) {
        LOGGER.debug("getById({})", id);
        return fileRepository.findById(id)
            .orElseThrow(() -> new NoRecordFoundException("id:%d", id));
    }

    /**
     * @param operation
     * @param file
     * @return
     */
    @Override
    public File validate(ServiceOperation operation, File file) {
        if (BeanUtils.isNull(file)) {
            throw new InvalidRequestException();
        }

        switch (operation) {
            case CREATE:
                if (BeanUtils.isNull(file.getName())) {
                    throw new InvalidRequestException();
                } else if (fileRepository.getByName(file.getName()).isPresent()) {
                    throw new DuplicateRecordException("name:%s", file.getName());
                }
                break;

            case UPDATE:
                if (BeanUtils.isNull(file.getId())) {
                    throw new InvalidRequestException();
                }
                break;
        }

        return file;
    }

    /**
     * @param file
     * @return
     */
    @Override
    public File create(File file) {
        LOGGER.debug("+create({})", file);
        validate(ServiceOperation.CREATE, file);
        // persist object
        file = fileRepository.saveAndFlush(file);
        LOGGER.debug("-create(), file:{}", file);
        return file;
    }

    /**
     * @param files
     * @return
     */
    @Override
    public List<File> create(List<File> files) {
        final List<File> createdFiles = new ArrayList<>();
        files.forEach(file -> createdFiles.add(create(file)));
        return createdFiles;
    }

    /**
     * @param filter
     * @return
     */
    @Override
    public List<File> getByFilter(Filter<File> filter) {
        return getByFilter(filter, null).getContent();
    }

    /**
     * @param filter
     * @param pageable
     * @return
     */
    @Override
    public Page<File> getByFilter(Filter<File> filter, Pageable pageable) {
        return fileRepository.findAll(pageable);
    }

    /**
     * @param file
     * @return
     */
    @Override
    public File update(File file) {
        LOGGER.debug("+update({})", file);
        validate(ServiceOperation.UPDATE, file);
        File oldFile = getById(file.getId());
        // update object
        BeanUtils.copyProperties(file, oldFile, IGNORED_PROPERTIES);
        // persist object
        file = fileRepository.saveAndFlush(oldFile);
        LOGGER.debug("-upsert(), file:{}", file);
        return file;
    }

    /**
     * @param files
     * @return
     */
    @Override
    public List<File> update(List<File> files) {
        final List<File> updatedFiles = new ArrayList<>();
        files.forEach(file -> updatedFiles.add(update(file)));
        return updatedFiles;
    }

    /**
     * @param name
     * @return
     */
    @Override
    public File getByName(String name) {
        Optional<File> file = fileRepository.getByName(name);
        if (!file.isPresent()) {
            throw new NoRecordFoundException("name:" + name);
        }

        return file.get();
    }

    /**
     * @param contents
     * @return
     */
    @Override
    public List<File> getByContents(String contents) {
        return fileRepository.getByContents(contents);
    }

    /**
     * @param id
     */
    @Override
    public File delete(final Long id) {
        LOGGER.debug("delete({})", id);
        Objects.requireNonNull(id);
        File file = getById(id);
        List<FileHistory> fileHistories = fileHistoryRepository.getAllByFileId(file.getId());
        LOGGER.info("Deleting {}", fileHistories);
        fileHistoryRepository.deleteAll(fileHistories);
        LOGGER.info("Deleting {}", file);
        fileRepository.deleteById(id);
        return file;
    }
}
