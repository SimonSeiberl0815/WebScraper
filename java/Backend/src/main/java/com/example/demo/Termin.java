package com.example.demo;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

import java.time.LocalDate;
import java.time.LocalTime;

@Entity
public class Termin {
    @Id
    private String terminKey;
    private String kursnummer;
    private String tag;
    private LocalDate datum;
    private LocalTime start;
    private LocalTime ende;
    private Double dauer;
    private String raum;
    private String leiter;
    private String studiengang;

    public Termin(String terminKey, String kursnummer, String tag, LocalDate datum, LocalTime start, LocalTime ende, Double dauer, String raum, String leiter, String studiengang) {
        this.terminKey = terminKey;
        this.kursnummer = kursnummer;
        this.tag = tag;
        this.datum = datum;
        this.start = start;
        this.ende = ende;
        this.dauer = dauer;
        this.raum = raum;
        this.leiter = leiter;
        this.studiengang = studiengang;
    }

    public Termin() {
    }

    public String getTerminKey() {
        return terminKey;
    }

    public void setTerminKey(String terminKey) {
        this.terminKey = terminKey;
    }

    public String getKursnummer() {
        return kursnummer;
    }

    public void setKursnummer(String kursnummer) {
        this.kursnummer = kursnummer;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public LocalDate getDatum() {
        return datum;
    }

    public void setDatum(LocalDate datum) {
        this.datum = datum;
    }

    public LocalTime getStart() {
        return start;
    }

    public void setStart(LocalTime start) {
        this.start = start;
    }

    public LocalTime getEnde() {
        return ende;
    }

    public void setEnde(LocalTime ende) {
        this.ende = ende;
    }

    public Double getDauer() {
        return dauer;
    }

    public void setDauer(Double dauer) {
        this.dauer = dauer;
    }

    public String getRaum() {
        return raum;
    }

    public void setRaum(String raum) {
        this.raum = raum;
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
}