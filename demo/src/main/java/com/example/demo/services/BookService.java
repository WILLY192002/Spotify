package com.example.demo.services;

import com.example.demo.controllers.request.BookCreateRequest;
import com.example.demo.repository.entity.Book;
import com.example.demo.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BookService {

    @Autowired
    private BookRepository bookRepository;
    public Book createBook(BookCreateRequest bookCreateRequest){
        Book book = Book.builder()
                .Title(bookCreateRequest.getTitle())
                .Author(bookCreateRequest.getAuthor())
                .Publisher(bookCreateRequest.getPublisher())
                .Genre(bookCreateRequest.getGenre())
                .PublicationYear(bookCreateRequest.getPublicationYear())
                .Synopsis(bookCreateRequest.getSynopsis())
                .build();
        return bookRepository.save(book);
    }
}