package com.rslakra.libraryservice.service.impl;

import com.rslakra.appsuite.core.BeanUtils;
import com.rslakra.appsuite.spring.exception.DuplicateRecordException;
import com.rslakra.appsuite.spring.exception.InvalidRequestException;
import com.rslakra.appsuite.spring.exception.NoRecordFoundException;
import com.rslakra.appsuite.spring.filter.Filter;
import com.rslakra.appsuite.spring.persistence.ServiceOperation;
import com.rslakra.appsuite.spring.service.AbstractServiceImpl;
import com.rslakra.libraryservice.enums.EntityStatus;
import com.rslakra.libraryservice.enums.RoleType;
import com.rslakra.libraryservice.persistence.entity.Role;
import com.rslakra.libraryservice.persistence.entity.User;
import com.rslakra.libraryservice.persistence.repository.RoleRepository;
import com.rslakra.libraryservice.persistence.repository.UserRepository;
import com.rslakra.libraryservice.service.UserService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import java.util.Set;

/**
 * @author Rohtash Lakra
 * @created 10/9/21 5:50 PM
 */
@Service
public class UserServiceImpl extends AbstractServiceImpl<User, Long> implements UserService {

    // LOGGER
    private static final Logger LOGGER = LoggerFactory.getLogger(UserServiceImpl.class);

    // userRepository
    private final UserRepository userRepository;
    // roleRepository
    private final RoleRepository roleRepository;

    /**
     * @param userRepository
     */
    @Autowired
    public UserServiceImpl(final UserRepository userRepository, final RoleRepository roleRepository) {
        this.userRepository = userRepository;
        this.roleRepository = roleRepository;
    }

    /**
     * Returns the list of all <code>T</code> objects.
     *
     * @return
     */
    @Override
    public List<User> getAll() {
        return userRepository.findAll();
    }

    /**
     * @param userId
     * @return
     */
    public User getById(final Long userId) {
        return userRepository.findById(userId)
            .orElseThrow(() -> new NoRecordFoundException("userId:%d", userId));
    }

    /**
     * @param operation
     * @param user
     * @return
     */
    @Override
    public User validate(ServiceOperation operation, User user) {
        if (BeanUtils.isNull(user)) {
            throw new InvalidRequestException();
        }

        switch (operation) {
            case CREATE:
                if (BeanUtils.isNull(user.getUserName())) {
                    throw new InvalidRequestException();
                } else if (userRepository.getByUserName(user.getUserName()).isPresent()) {
                    throw new DuplicateRecordException("userName:%s", user.getUserName());
                }
                break;

            case UPDATE:
                if (BeanUtils.isNull(user.getId())) {
                    throw new InvalidRequestException();
                }
                break;
        }

        return user;
    }

    /**
     * @param user
     * @return
     */
    @Override
    public User create(User user) {
        LOGGER.debug("+create({})", user);
        validate(ServiceOperation.CREATE, user);
        // persist object
        user = userRepository.saveAndFlush(user);
        LOGGER.debug("-create(), user:{}", user);
        return user;
    }

    /**
     * @param users
     * @return
     */
    @Override
    public List<User> create(List<User> users) {
        LOGGER.debug("+create({})", users);
        Objects.requireNonNull(users);
        final List<User> createdUsers = new ArrayList<>();
        users.forEach(user -> createdUsers.add(create(user)));
        LOGGER.debug("-create(), createdUsers:{}", createdUsers);
        return createdUsers;
    }

    /**
     * @param filter
     * @return
     */
    @Override
    public List<User> getByFilter(Filter<User> filter) {
        return getByFilter(filter, null).getContent();
    }

    /**
     * @param filter
     * @param pageable
     * @return
     */
    @Override
    public Page<User> getByFilter(Filter<User> filter, Pageable pageable) {
        return userRepository.findAll(pageable);
    }

    /**
     * @param user
     * @return
     */
    @Override
    public User update(User user) {
        LOGGER.debug("+update({})", user);
        validate(ServiceOperation.UPDATE, user);
        User oldUser = getById(user.getId());
        // update object
        BeanUtils.copyProperties(user, oldUser, IGNORED_PROPERTIES);
        // persist user
        user = userRepository.saveAndFlush(oldUser);
        LOGGER.debug("-update(), user:{}", user);
        return user;
    }

    /**
     * @param users
     * @return
     */
    @Override
    public List<User> update(List<User> users) {
        LOGGER.debug("+update({})", users);
        Objects.requireNonNull(users);
        final List<User> updatedUsers = new ArrayList<>();
        users.forEach(user -> updatedUsers.add(update(user)));
        LOGGER.debug("-update(), updatedUsers:{}", updatedUsers);
        return updatedUsers;
    }

    /**
     * Returns the list of users by userName.
     *
     * @param userName
     * @return
     */
    public User getByUserName(String userName) {
        LOGGER.debug("getByUserName({})", userName);
        Objects.requireNonNull(userName);
        Optional<User> user = userRepository.getByUserName(userName);
        if (!user.isPresent()) {
            throw new NoRecordFoundException("userName:" + userName);
        }

        return user.get();
    }

    /**
     * Returns the list of users by firstName.
     *
     * @param firstName
     * @return
     */
    public List<User> getByFirstName(String firstName) {
        LOGGER.debug("getByFirstName({})", firstName);
        Objects.requireNonNull(firstName);
        return userRepository.getByFirstName(firstName);
    }

    /**
     * Returns the list of users by lastName.
     *
     * @param lastName
     * @return
     */
    public List<User> getByLastName(String lastName) {
        LOGGER.debug("getByLastName({})", lastName);
        Objects.requireNonNull(lastName);
        return userRepository.getByLastName(lastName);
    }

    /**
     * Returns the user by email.
     *
     * @param email
     * @return
     */
    public User getByEmail(final String email) {
        LOGGER.debug("getByEmail({})", email);
        Objects.requireNonNull(email);
        return userRepository.getByEmail(email).orElseThrow(() -> new NoRecordFoundException("email:%s", email));
    }

    /**
     * Returns the list of users by email.
     *
     * @param emailList
     * @return
     */
    @Override
    public List<User> getByEmails(List<String> emailList) {
        LOGGER.debug("getByEmails({})", emailList);
        Objects.requireNonNull(emailList);
        return userRepository.getByEmails(emailList);
    }

    /**
     * @param userId
     */
    public User delete(Long userId) {
        LOGGER.debug("delete({})", userId);
        Objects.requireNonNull(userId);
        User user = getById(userId);
        LOGGER.debug("Deleting {}", user);
        userRepository.deleteById(userId);
        return user;
    }

    /**
     * Returns the <code>Role</code> by <code>roleType</code>.
     *
     * @param roleType
     * @return
     */
    private Optional<Role> loadByRoleType(final RoleType roleType) {
        return roleRepository.findByName(roleType.name());
    }

    /**
     * @param user
     * @param roleTypes
     * @return
     */
    @Override
    public void addRoles(final User user, RoleType... roleTypes) {
        if (!BeanUtils.isEmpty(roleTypes)) {
            final Set<Role> userRoles = new HashSet<>();
            Arrays.asList(roleTypes).forEach(roleType -> {
                final Optional<Role> roleFromDB = loadByRoleType(roleType);
                if (roleFromDB.isPresent() && EntityStatus.ACTIVE == roleFromDB.get().getStatus()) {
                    userRoles.add(roleFromDB.get());
                }
            });

            // add roles to the user
            user.addRoles(userRoles);
        }
    }

    /**
     * @param user
     * @param roleTypes
     * @return
     */
    @Override
    public boolean hasRoles(final User user, final Set<RoleType> roleTypes) {
        return user.hasRoles(RoleType.ofRoleTypes(roleTypes));
    }
}
