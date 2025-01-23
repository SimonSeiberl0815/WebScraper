package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/studiengang")
public class StudiengangController {

    @Autowired
    private StudiengangRepository studiengangRepository;

    // Create a new Studiengang
    @PostMapping
    public ResponseEntity<Studiengang> createStudiengang(@RequestBody Studiengang studiengang) {
        Studiengang savedStudiengang = studiengangRepository.save(studiengang);
        return ResponseEntity.ok(savedStudiengang);
    }

    // Get all Studiengänge
    @GetMapping
    public List<Studiengang> getAllStudiengänge() {
        return studiengangRepository.findAll();
    }

    // Get a specific Studiengang by SKZ
    @GetMapping("/{skz}")
    public ResponseEntity<Studiengang> getStudiengangBySkz(@PathVariable Long skz) {
        Optional<Studiengang> studiengang = studiengangRepository.findById(skz);
        return studiengang.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // Update a Studiengang by SKZ
    @PutMapping("/{skz}")
    public ResponseEntity<Studiengang> updateStudiengang(@PathVariable Long skz, @RequestBody Studiengang updatedStudiengang) {
        if (!studiengangRepository.existsById(skz)) {
            return ResponseEntity.notFound().build();
        }

        updatedStudiengang.setSkz(skz); // Set the ID to ensure it updates the correct record
        Studiengang savedStudiengang = studiengangRepository.save(updatedStudiengang);
        return ResponseEntity.ok(savedStudiengang);
    }

    // Delete a Studiengang by SKZ
    @DeleteMapping("/{skz}")
    public ResponseEntity<Void> deleteStudiengang(@PathVariable Long skz) {
        if (!studiengangRepository.existsById(skz)) {
            return ResponseEntity.notFound().build();
        }

        studiengangRepository.deleteById(skz);
        return ResponseEntity.noContent().build();
    }
}
