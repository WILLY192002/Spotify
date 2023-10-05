package com.example.demo.repository.entity;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;
import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Document(collection = "Book")
public class Book implements Serializable {
    @Id
    private String id;
    private String Title;
    private String Author;
    private String Publisher;
    private List<String> Genre;
    private String PublicationYear;
    private String Synopsis;
}