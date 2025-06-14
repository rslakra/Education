package com.rslakra.libraryservice.controller.web;

import com.rslakra.appsuite.spring.exception.InvalidRequestException;
import com.rslakra.libraryservice.persistence.entity.Role;
import com.rslakra.libraryservice.service.RoleService;
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
@RequestMapping("/roles")
public class RoleWebController extends AbstractWebController<Role> {

    // roleService
    private final RoleService roleService;

    /**
     * @param roleService
     */
    @Autowired
    public RoleWebController(RoleService roleService) {
        this.roleService = roleService;
    }

    /**
     * @param role
     * @return
     */
    @PostMapping("/save")
    @Override
    public String save(Role role) {
        if (Objects.isNull(role)) {
            throw new InvalidRequestException();
        } else if (Objects.nonNull(role.getId())) {
            role = roleService.update(role);
        } else {
            role = roleService.create(role);
        }

        return "redirect:/roles/list";
    }

    /**
     * @param model
     * @return
     */
    @GetMapping("/list")
    @Override
    public String listObjects(Model model) {
        List<Role> roles = roleService.getAll();
        model.addAttribute("roles", roles);
        return "roles/listRoles";
    }

    /**
     * @param model
     * @param id
     * @return
     */
    @GetMapping(path = {"/create", "/update/{id}"})
    @Override
    public String upsert(Model model, @PathVariable(name = "id", required = false) Optional<Long> id) {
        Role role = null;
        if (id.isPresent()) {
            role = roleService.getById(id.get());
        } else {
            role = new Role();
        }
        model.addAttribute("role", role);

        return "roles/editRole";
    }

    /**
     * @param model
     * @param id
     * @return
     */
    @RequestMapping("/delete/{id}")
    @Override
    public String delete(Model model, @PathVariable(name = "id") Long id) {
        roleService.delete(id);
        return "redirect:/roles/list";
    }

}
