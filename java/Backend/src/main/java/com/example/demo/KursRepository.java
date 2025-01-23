package com.example.demo;



import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface KursRepository extends JpaRepository<Kurs, String> {

    List<Kurs> findByStudiengang(String studiengang);

}
