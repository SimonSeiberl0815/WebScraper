package com.example.demo;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
@Entity
public class Kurs {
    @Id
    private String kursnummer;
    private String lva;
    private String name;
    private String leiter;
    private String url;
    private String studiengang;


    public Kurs(){}

    public Kurs(String kursnummer, String lva,String name, String leiter, String url, String studiengang) {
        this.kursnummer = kursnummer;
        this.lva = lva;
        this.name = name;
        this.leiter = leiter;
        this.url = url;
        this.studiengang = studiengang;

    }

    public String getKursnummer() {
        return kursnummer;
    }

    public void setKursnummer(String kursnummer) {
        this.kursnummer = kursnummer;
    }

    public String getLva() {
        return lva;
    }

    public void setLva(String lva) {
        this.lva = lva;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLeiter() {
        return leiter;
    }

    public void setLeiter(String leiter) {
        this.leiter = leiter;
    }

    public String getStudiengang() {
        return studiengang;
    }

    public void setStudiengang(String studiengang) {
        this.studiengang = studiengang;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
}
