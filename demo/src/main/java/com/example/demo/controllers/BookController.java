package com.example.demo.controllers;

import com.example.demo.controllers.request.BookCreateRequest;
import com.example.demo.services.BookService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.parameters.RequestBody;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/book")
public class BookController {
    @Autowired
    BookService bookService;

    @PostMapping()
    @Operation(summary = "This method is used to create a book" )

    public ResponseEntity<?> createBook(@RequestBody BookCreateRequest bookCreateRequest){
        return ResponseEntity.ok(bookService.createBook(bookCreateRequest));
    }
}