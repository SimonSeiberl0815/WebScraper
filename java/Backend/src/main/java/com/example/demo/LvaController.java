package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/lva")
public class LvaController {

    @Autowired
    private LvaRepository lvaRepository;

    // Create new LVA
    @PostMapping
    public Lva createLva(@RequestBody LvaCreateRequest request) {
        Lva lva = new Lva();
        lva.setLvanummer(request.getLvanummer());
        lva.setName(request.getName());
        lva.setTyp(request.getTyp());
        lva.setStudiengang(request.getStudiengang());
        lva.setModul(request.getModul());
        lva.setEtcs(request.getEtcs());
        lva.setVerantwortlicher(request.getVerantwortlicher());
        lva.setUrl(request.getUrl());
        lva.setJahr(request.getJahr());
        lva.setStunden(request.getStunden());
        lva.setUniversitaet(request.getUniversitaet());
        lva.setVorraussetzungen(request.getVorraussetzungen());
        lva.setZiele(request.getZiele());
        lva.setInhalte(request.getInhalte());
        lva.setBeurteilung(request.getBeurteilung());
        lva.setLehrmethoden(request.getLehrmethoden());
        lva.setSprache(request.getSprache());
        lva.setLiteratur(request.getLiteratur());
        return lvaRepository.save(lva);
    }

    // Get all LVAs
    @GetMapping
    public List<Lva> getAllLvas() {
        return lvaRepository.findAll();
    }

    @GetMapping("/studiengang/{studiengang}")
    public List<Lva> getLvaByStudiengang(@PathVariable String studiengang) {
        return lvaRepository.findByStudiengang(studiengang);
    }

    // Get LVA by ID
    @GetMapping("/{lvanummer}")
    public ResponseEntity<Lva> getLvaById(@PathVariable("lvanummer") String id) {
        return lvaRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // Update existing LVA
    @PutMapping("/{lvanummer}")
    public ResponseEntity<Lva> updateLva(@PathVariable String id, @RequestBody LvaCreateRequest request) {
        return lvaRepository.findById(id).map(existingLva -> {
            existingLva.setName(request.getName());
            existingLva.setTyp(request.getTyp());
            existingLva.setStudiengang(request.getStudiengang());
            existingLva.setModul(request.getModul());
            existingLva.setUrl(request.getUrl());
            existingLva.setVorraussetzungen(request.getVorraussetzungen());
            existingLva.setZiele(request.getZiele());
            existingLva.setInhalte(request.getInhalte());
            existingLva.setBeurteilung(request.getBeurteilung());
            existingLva.setLehrmethoden(request.getLehrmethoden());
            existingLva.setSprache(request.getSprache());
            existingLva.setLiteratur(request.getLiteratur());
            return ResponseEntity.ok(lvaRepository.save(existingLva));
        }).orElse(ResponseEntity.notFound().build());
    }

    // Delete LVA
    @DeleteMapping("/{lvanummer}")
    public ResponseEntity<Void> deleteLva(@PathVariable String lvanummer) {
        Optional<Lva> lva = lvaRepository.findById(lvanummer);

        if (lva.isPresent()) {
            lvaRepository.delete(lva.get());
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
    }
}
