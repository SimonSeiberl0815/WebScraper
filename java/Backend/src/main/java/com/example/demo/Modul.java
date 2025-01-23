package com.example.demo;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Lob;

@Entity
public class Modul {
    @Id
    private String modulnummer;
    private String name;

    @Lob
    private byte[] vorraussetzungen;   // Store binary data
    @Lob
    private byte[] ziele;              // Store binary data
    @Lob
    private byte[] lerninhalte;        // Store binary data
    @Lob
    private byte[] infos;              // Store binary data

    private String studiengang;
    private byte[] books;
    private String url;

    public Modul() {}

    public Modul(String modulnummer, String name, byte[] vorraussetzungen, byte[] ziele, byte[] lerninhalte, byte[] infos, String studiengang, byte[] books, String url) {
        this.modulnummer = modulnummer;
        this.name = name;
        this.vorraussetzungen = vorraussetzungen;
        this.ziele = ziele;
        this.lerninhalte = lerninhalte;
        this.infos = infos;
        this.studiengang = studiengang;
        this.books = books;
        this.url = url;
    }

    public String getModulnummer() {
        return modulnummer;
    }

    public void setModulnummer(String modulnummer) {
        this.modulnummer = modulnummer;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public byte[] getVorraussetzungen() {
        return vorraussetzungen;
    }

    public void setVorraussetzungen(byte[] vorraussetzungen) {
        this.vorraussetzungen = vorraussetzungen;
    }

    public byte[] getZiele() {
        return ziele;
    }

    public void setZiele(byte[] ziele) {
        this.ziele = ziele;
    }

    public byte[] getLerninhalte() {
        return lerninhalte;
    }

    public void setLerninhalte(byte[] lerninhalte) {
        this.lerninhalte = lerninhalte;
    }

    public byte[] getInfos() {
        return infos;
    }

    public void setInfos(byte[] infos) {
        this.infos = infos;
    }

    public String getStudiengang() {
        return studiengang;
    }

    public void setStudiengang(String studiengang) {
        this.studiengang = studiengang;
    }

    public byte[] getBooks() {
        return books;
    }

    public void setBooks(byte[] books) {
        this.books = books;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
}
