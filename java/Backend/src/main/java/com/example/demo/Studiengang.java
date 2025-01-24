package com.example.demo;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Studiengang {
    @Id
    private String skz;
    private String name;
    private String level;
    private String url;

    public Studiengang(){}

    public Studiengang(String skz, String name, String level, String url) {
        this.skz = skz;
        this.name = name;
        this.level = level;
        this.url = url;
    }

    public String getSkz() {
        return skz;
    }

    public void setSkz(String skz) {
        this.skz = skz;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
}
