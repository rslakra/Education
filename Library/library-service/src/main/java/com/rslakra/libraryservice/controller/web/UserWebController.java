package com.rslakra.libraryservice.controller.web;

import com.rslakra.appsuite.spring.exception.InvalidRequestException;
import com.rslakra.libraryservice.persistence.entity.Role;
import com.rslakra.libraryservice.persistence.entity.User;
import com.rslakra.libraryservice.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 * @author: Rohtash Lakra
  * @since 09/30/2019 05:38 PM
 */
@Controller
@RequestMapping("/users")
public class UserWebController extends AbstractWebController<Role> {

    // userService
    private final UserService userService;

    /**
     * @param userService
     */
    @Autowired
    public UserWebController(UserService userService) {
        this.userService = userService;
    }

    /**
     * @param user
     * @return
     */
    @PostMapping("/save")
    public String saveUser(User user) {
        if (Objects.isNull(user)) {
            throw new InvalidRequestException();
        } else if (Objects.nonNull(user.getId())) {
            user = userService.update(user);
        } else {
            user = userService.create(user);
        }

        return "redirect:/users/list";
    }

    /**
     * @param model
     * @return
     */
    @GetMapping("/list")
    public String getUsers(Model model) {
        List<User> users = userService.getAll();
        model.addAttribute("users", users);
        return "users/listUsers";
    }

    /**
     * @param model
     * @param userId
     * @return
     */
    @GetMapping(path = {"/create", "/update/{userId}"})
    public String upsertUser(Model model, @PathVariable(name = "userId") Optional<Long> userId) {
        User user = null;
        if (userId.isPresent()) {
            user = userService.getById(userId.get());
        } else {
            user = new User();
        }
        model.addAttribute("user", user);

        return "users/editUser";
    }

    /**
     * @param model
     * @param userId
     * @return
     */
    @RequestMapping("/delete/{userId}")
    public String delete(Model model, @PathVariable(name = "userId") Long userId) {
        userService.delete(userId);
        return "redirect:/users/list";
    }


}
