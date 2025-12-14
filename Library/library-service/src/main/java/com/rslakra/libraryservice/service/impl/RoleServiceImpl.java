package com.rslakra.libraryservice.service.impl;

import com.rslakra.appsuite.core.BeanUtils;
import com.rslakra.appsuite.spring.exception.DuplicateRecordException;
import com.rslakra.appsuite.spring.exception.InvalidRequestException;
import com.rslakra.appsuite.spring.exception.NoRecordFoundException;
import com.rslakra.appsuite.spring.filter.Filter;
import com.rslakra.appsuite.spring.persistence.ServiceOperation;
import com.rslakra.appsuite.spring.service.AbstractServiceImpl;
import com.rslakra.libraryservice.persistence.entity.Role;
import com.rslakra.libraryservice.persistence.repository.RoleRepository;
import com.rslakra.libraryservice.service.RoleService;
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
public class RoleServiceImpl extends AbstractServiceImpl<Role, Long> implements RoleService {

    // LOGGER
    private static final Logger LOGGER = LoggerFactory.getLogger(RoleServiceImpl.class);

    // roleRepository
    private final RoleRepository roleRepository;

    /**
     * @param roleRepository
     */
    @Autowired
    public RoleServiceImpl(final RoleRepository roleRepository) {
        this.roleRepository = roleRepository;
    }

    /**
     * @return
     */
    @Override
    public List<Role> getAll() {
        final List<Role> roles = roleRepository.findAll();
        LOGGER.debug("getAllObjects(), roles:{}", roles);
        return roles;
    }

    /**
     * @param id
     * @return
     */
    @Override
    public Role getById(Long id) {
        LOGGER.debug("getById({})", id);
        return roleRepository.findById(id).orElseThrow(() -> new NoRecordFoundException("id:%d", id));
    }

    /**
     * @param operation
     * @param role
     * @return
     */
    @Override
    public Role validate(ServiceOperation operation, Role role) {
        if (BeanUtils.isNull(role)) {
            throw new InvalidRequestException();
        }

        switch (operation) {
            case CREATE:
                if (BeanUtils.isNull(role.getName())) {
                    throw new InvalidRequestException();
                } else if (roleRepository.findByName(role.getName()).isPresent()) {
                    throw new DuplicateRecordException("name:%s", role.getName());
                }
                break;

            case UPDATE:
                if (BeanUtils.isNull(role.getId())) {
                    throw new InvalidRequestException();
                }
                break;
        }

        return role;
    }

    /**
     * @param role
     * @return
     */
    @Override
    public Role create(Role role) {
        LOGGER.debug("+create({})", role);
        validate(ServiceOperation.CREATE, role);
        // persist object
        role = roleRepository.saveAndFlush(role);
        LOGGER.debug("-create(), role:{}", role);
        return role;
    }

    /**
     * @param roles
     * @return
     */
    @Override
    public List<Role> create(List<Role> roles) {
        final List<Role> createdRoles = new ArrayList<>();
        roles.forEach(role -> createdRoles.add(create(role)));
        return createdRoles;
    }

    /**
     * @param filter
     * @return
     */
    @Override
    public List<Role> getByFilter(Filter<Role> filter) {
        return getByFilter(filter, null).getContent();
    }

    /**
     * @param filter
     * @param pageable
     * @return
     */
    @Override
    public Page<Role> getByFilter(Filter<Role> filter, Pageable pageable) {
        return roleRepository.findAll(pageable);
    }

    /**
     * @param role
     * @return
     */
    @Override
    public Role update(Role role) {
        LOGGER.debug("+update({})", role);
        validate(ServiceOperation.UPDATE, role);
        Role oldRole = getById(role.getId());
        // update object
        BeanUtils.copyProperties(role, oldRole, IGNORED_PROPERTIES);
        // persist user
        role = roleRepository.saveAndFlush(oldRole);
        LOGGER.debug("-update(), role:{}", role);
        return role;
    }

    /**
     * @param roles
     * @return
     */
    @Override
    public List<Role> update(List<Role> roles) {
        final List<Role> updatedRoles = new ArrayList<>();
        roles.forEach(role -> updatedRoles.add(update(role)));
        return updatedRoles;
    }

    /**
     * @param name
     * @return
     */
    @Override
    public Role getByName(final String name) {
        Optional<Role> role = roleRepository.findByName(name);
        if (!role.isPresent()) {
            throw new NoRecordFoundException("name:" + name);
        }

        return role.get();
    }

    /**
     * @param status
     * @return
     */
    @Override
    public List<Role> getByStatus(String status) {
        return roleRepository.getByStatus(status);
    }

    /**
     * @param id
     * @return
     */
    @Override
    public Role delete(Long id) {
        LOGGER.debug("delete({})", id);
        Objects.requireNonNull(id);
        Role role = getById(id);
        LOGGER.info("Deleting {}", role);
        roleRepository.deleteById(id);
        return role;
    }
}
