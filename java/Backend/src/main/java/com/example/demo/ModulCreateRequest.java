package com.example.demo;

public class ModulCreateRequest {
    private String modulnummer;
    private String name;
    private byte[] vorraussetzungen;  // compressed binary data
    private byte[] ziele;              // compressed binary data
    private byte[] lerninhalte;        // compressed binary data
    private byte[] infos;              // compressed binary data
    private String studiengang;
    private byte[] books;
    private String url;

    // Getters and Setters

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
