package com.example.demo;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ModulRepository extends JpaRepository<Modul, String> {
    // You can add custom queries here if necessary
    List<Modul> findByStudiengang(String studiengang);
}
