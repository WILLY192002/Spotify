package com.example.demo.controllers.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

import java.util.ArrayList;

@Data
public class BookCreateRequest {
    @JsonProperty
    private String Title;

    @JsonProperty
    private String Author;

    @JsonProperty
    private String Publisher;

    @JsonProperty
    private ArrayList<String> Genre;

    @JsonProperty
    private String PublicationYear;

    @JsonProperty
    private String Synopsis;
}