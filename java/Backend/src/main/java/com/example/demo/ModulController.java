package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/modul")
public class ModulController {

    @Autowired
    private ModulRepository modulRepository;

    // Create a new Modul
    @PostMapping
    public ResponseEntity<Modul> createModul(@RequestBody ModulCreateRequest modulCreateRequest) {
        Modul modul = new Modul();

        // Set the simple fields directly
        modul.setModulnummer(modulCreateRequest.getModulnummer());
        modul.setName(modulCreateRequest.getName());
        modul.setStudiengang(modulCreateRequest.getStudiengang());
        modul.setBooks(modulCreateRequest.getBooks());
        modul.setUrl(modulCreateRequest.getUrl());

        // Set the compressed fields (binary data)
        modul.setVorraussetzungen(modulCreateRequest.getVorraussetzungen());  // byte[]
        modul.setZiele(modulCreateRequest.getZiele());                          // byte[]
        modul.setLerninhalte(modulCreateRequest.getLerninhalte());              // byte[]
        modul.setInfos(modulCreateRequest.getInfos());                          // byte[]

        Modul savedModul = modulRepository.save(modul);
        return new ResponseEntity<>(savedModul, HttpStatus.CREATED);
    }

    // Get all Moduls
    @GetMapping
    public List<Modul> getAllModuls() {
        return modulRepository.findAll();
    }

    @GetMapping("/studiengang/{studiengang}")
    public List<Modul> getLvaByStudiengang(@PathVariable String studiengang) {
        return modulRepository.findByStudiengang(studiengang);
    }

    // Get a specific Modul by modulNummer
    @GetMapping("/{modulnummer}")
    public ResponseEntity<Modul> getModulByModulNummer(@PathVariable String modulnummer) {
        Optional<Modul> modul = modulRepository.findById(modulnummer);
        return modul.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.status(HttpStatus.NOT_FOUND).build());
    }

    // Update an existing Modul
    @PutMapping("/{modulnummer}")
    public ResponseEntity<Modul> updateModul(@PathVariable String modulNummer, @RequestBody ModulCreateRequest modulCreateRequest) {
        Optional<Modul> optionalModul = modulRepository.findById(modulNummer);

        if (optionalModul.isPresent()) {
            Modul existingModul = optionalModul.get();
            existingModul.setName(modulCreateRequest.getName());
            existingModul.setStudiengang(modulCreateRequest.getStudiengang());
            existingModul.setBooks(modulCreateRequest.getBooks());
            existingModul.setUrl(modulCreateRequest.getUrl());

            // Set the compressed fields (binary data)
            existingModul.setVorraussetzungen(modulCreateRequest.getVorraussetzungen());  // byte[]
            existingModul.setZiele(modulCreateRequest.getZiele());                          // byte[]
            existingModul.setLerninhalte(modulCreateRequest.getLerninhalte());              // byte[]
            existingModul.setInfos(modulCreateRequest.getInfos());                          // byte[]

            Modul updatedModul = modulRepository.save(existingModul);
            return ResponseEntity.ok(updatedModul);
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
    }

    // Delete a Modul by modulNummer
    @DeleteMapping("/{modulnummer}")
    public ResponseEntity<Void> deleteModul(@PathVariable String modulNummer) {
        Optional<Modul> modul = modulRepository.findById(modulNummer);

        if (modul.isPresent()) {
            modulRepository.delete(modul.get());
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
    }
}
