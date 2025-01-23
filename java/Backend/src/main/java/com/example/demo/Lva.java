package com.example.demo;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Lob;

@Entity
public class Lva {
    @Id
    private String lvanummer;
    private String name;
    private String typ;
    private String studiengang;
    private String modul;
    private String etcs;
    private String verantwortlicher;
    private String jahr;
    private String stunden;
    private String universitaet;
    private String url;
    @Lob
    private byte[] vorraussetzungen;
    @Lob
    private byte[] ziele;
    @Lob
    private byte[] inhalte;
    @Lob
    private byte[] beurteilung;
    @Lob
    private byte[] lehrmethoden;
    @Lob
    private byte[] sprache;
    @Lob
    private byte[] literatur;

    public Lva(){}

    public Lva(String lvanummer, String name, String typ, String studiengang, String modul,String etcs, String verantwortlicher,String jahr, String stunden, String universitaet, String url, byte[] vorraussetzungen, byte[] ziele, byte[] inhalte, byte[] beurteilung, byte[] lehrmethoden, byte[] sprache, byte[] literatur) {
        this.lvanummer = lvanummer;
        this.name = name;
        this.typ = typ;
        this.studiengang = studiengang;
        this.modul = modul;
        this.etcs = etcs;
        this.verantwortlicher = verantwortlicher;
        this.jahr = jahr;
        this.stunden = stunden;
        this.universitaet = universitaet;
        this.url = url;
        this.vorraussetzungen = vorraussetzungen;
        this.ziele = ziele;
        this.inhalte = inhalte;
        this.beurteilung = beurteilung;
        this.lehrmethoden = lehrmethoden;
        this.sprache = sprache;
        this.literatur = literatur;
    }

    public String getLvanummer() {
        return lvanummer;
    }

    public void setLvanummer(String lvanummer) {
        this.lvanummer = lvanummer;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getTyp() {
        return typ;
    }

    public void setTyp(String typ) {
        this.typ = typ;
    }

    public String getStudiengang() {
        return studiengang;
    }

    public void setStudiengang(String studiengang) {
        this.studiengang = studiengang;
    }

    public String getModul() {
        return modul;
    }

    public void setModul(String modul) {
        this.modul = modul;
    }

    public String getEtcs() {
        return etcs;
    }

    public void setEtcs(String etcs) {
        this.etcs = etcs;
    }

    public String getVerantwortlicher() {
        return verantwortlicher;
    }

    public void setVerantwortlicher(String verantwortlicher) {
        this.verantwortlicher = verantwortlicher;
    }

    public String getJahr() {
        return jahr;
    }

    public void setJahr(String jahr) {
        this.jahr = jahr;
    }

    public String getStunden() {
        return stunden;
    }

    public void setStunden(String stunden) {
        this.stunden = stunden;
    }

    public String getUniversitaet() {
        return universitaet;
    }

    public void setUniversitaet(String universitaet) {
        this.universitaet = universitaet;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
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

    public byte[] getInhalte() {
        return inhalte;
    }

    public void setInhalte(byte[] inhalte) {
        this.inhalte = inhalte;
    }

    public byte[] getBeurteilung() {
        return beurteilung;
    }

    public void setBeurteilung(byte[] beurteilung) {
        this.beurteilung = beurteilung;
    }

    public byte[] getLehrmethoden() {
        return lehrmethoden;
    }

    public void setLehrmethoden(byte[] lehrmethoden) {
        this.lehrmethoden = lehrmethoden;
    }

    public byte[] getSprache() {
        return sprache;
    }

    public void setSprache(byte[] sprache) {
        this.sprache = sprache;
    }

    public byte[] getLiteratur() {
        return literatur;
    }

    public void setLiteratur(byte[] literatur) {
        this.literatur = literatur;
    }
}