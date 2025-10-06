package com.rslakra.libraryservice.controller.web;

import com.rslakra.appsuite.spring.exception.InvalidRequestException;
import com.rslakra.libraryservice.persistence.entity.File;
import com.rslakra.libraryservice.service.FileService;
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
@RequestMapping("/files")
public class FileWebController extends AbstractWebController<File> {

    // fileService
    private final FileService fileService;

    /**
     * @param fileService
     */
    @Autowired
    public FileWebController(FileService fileService) {
        this.fileService = fileService;
    }

    /**
     * @param file
     * @return
     */
    @PostMapping("/save")
    @Override
    public String save(File file) {
        if (Objects.isNull(file)) {
            throw new InvalidRequestException();
        } else if (Objects.nonNull(file.getId())) {
            file = fileService.update(file);
        } else {
            file = fileService.create(file);
        }

        return "redirect:/files/list";
    }

    /**
     * @param model
     * @return
     */
    @GetMapping("/list")
    @Override
    public String listObjects(Model model) {
        List<File> files = fileService.getAll();
        model.addAttribute("files", files);
        return "files/listFiles";
    }

    /**
     * @param model
     * @param id
     * @return
     */
    @GetMapping(path = {"/create", "/update/{id}"})
    @Override
    public String upsert(Model model, @PathVariable(name = "id", required = false) Optional<Long> id) {
        File file = null;
        if (id.isPresent()) {
            file = fileService.getById(id.get());
        } else {
            file = new File();
        }
        model.addAttribute("file", file);

        return "files/editFile";
    }

    /**
     * @param model
     * @param id
     * @return
     */
    @RequestMapping("/delete/{id}")
    @Override
    public String delete(Model model, @PathVariable(name = "id") Long id) {
        fileService.delete(id);
        return "redirect:/files/list";
    }

}
