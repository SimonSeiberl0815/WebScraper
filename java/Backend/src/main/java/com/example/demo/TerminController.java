package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/termin")
public class TerminController {

    @Autowired
    private TerminRepository terminRepository;

    // Create a new Termin
    @PostMapping
    public ResponseEntity<Termin> createTermin(@RequestBody Termin termin) {
        Termin savedTermin = terminRepository.save(termin);
        return ResponseEntity.ok(savedTermin);
    }

    // Get all Termine
    @GetMapping
    public List<Termin> getAllTermine() {
        return terminRepository.findAll();
    }

    @GetMapping("/studiengang/{studiengang}")
    public List<Termin> getLvaByStudiengang(@PathVariable String studiengang) {
        return terminRepository.findByStudiengang(studiengang);
    }

    // Get a specific Termin by key
    @GetMapping("/{terminKey}")
    public ResponseEntity<Termin> getTerminByKey(@PathVariable String terminKey) {
        Optional<Termin> termin = terminRepository.findById(terminKey);
        return termin.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // Update a Termin by key
    @PutMapping("/{terminKey}")
    public ResponseEntity<Termin> updateTermin(@PathVariable String terminKey, @RequestBody Termin updatedTermin) {
        if (!terminRepository.existsById(terminKey)) {
            return ResponseEntity.notFound().build();
        }

        updatedTermin.setTerminKey(terminKey); // Set the key to ensure it updates the correct record
        Termin savedTermin = terminRepository.save(updatedTermin);
        return ResponseEntity.ok(savedTermin);
    }

    // Delete a Termin by key
    @DeleteMapping("/{terminKey}")
    public ResponseEntity<Void> deleteTermin(@PathVariable String terminKey) {
        if (!terminRepository.existsById(terminKey)) {
            return ResponseEntity.notFound().build();
        }

        terminRepository.deleteById(terminKey);
        return ResponseEntity.noContent().build();
    }
}
