package com.example.demo;

import com.example.demo.Lva;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LvaRepository extends JpaRepository<Lva, String> {
    // Additional custom query methods (if needed) can be defined here
    List<Lva> findByStudiengang(String studiengang);
}