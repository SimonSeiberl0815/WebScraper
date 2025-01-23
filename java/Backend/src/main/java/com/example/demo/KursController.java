package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/kurs")
public class KursController {

    @Autowired
    private KursRepository kursRepository;

    // Create a new Kurs
    @PostMapping
    public ResponseEntity<Kurs> createKurs(@RequestBody Kurs kurs) {
        Kurs savedKurs = kursRepository.save(kurs);
        return ResponseEntity.ok(savedKurs);
    }

    // Get all Kurse
    @GetMapping
    public List<Kurs> getAllKurse() {
        return kursRepository.findAll();
    }

    @GetMapping("/studiengang/{studiengang}")
    public List<Kurs> getLvaByStudiengang(@PathVariable String studiengang) {
        return kursRepository.findByStudiengang(studiengang);
    }

    // Get a specific Kurs by kursnummer
    @GetMapping("/{kursnummer}")
    public ResponseEntity<Kurs> getKursByKursnummer(@PathVariable String kursnummer) {
        Optional<Kurs> kurs = kursRepository.findById(kursnummer);
        return kurs.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // Update a Kurs by kursnummer
    @PutMapping("/{kursnummer}")
    public ResponseEntity<Kurs> updateKurs(@PathVariable String kursnummer, @RequestBody Kurs updatedKurs) {
        if (!kursRepository.existsById(kursnummer)) {
            return ResponseEntity.notFound().build();
        }

        updatedKurs.setKursnummer(kursnummer); // Set the ID to ensure it updates the correct record
        Kurs savedKurs = kursRepository.save(updatedKurs);
        return ResponseEntity.ok(savedKurs);
    }

    // Delete a Kurs by kursnummer
    @DeleteMapping("/{kursnummer}")
    public ResponseEntity<Void> deleteKurs(@PathVariable String kursnummer) {
        if (!kursRepository.existsById(kursnummer)) {
            return ResponseEntity.notFound().build();
        }

        kursRepository.deleteById(kursnummer);
        return ResponseEntity.noContent().build();
    }
}
