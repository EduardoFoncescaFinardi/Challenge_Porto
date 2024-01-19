package br.com.domain.service;

import br.com.domain.entity.Bicicleta;
import br.com.domain.repository.BicicletaRepository;

import java.util.List;
import java.util.Objects;

public class BicicletaService implements Service<Bicicleta, Long> {

    private BicicletaRepository repository;

    public BicicletaService(){
        this.repository = new BicicletaRepository();
    }
    @Override
    public List<Bicicleta> findAll(){
        return repository.findAll();
    }
    @Override
    public Bicicleta findById(Long id){
        return repository.findById(id);
    }
    @Override
    public List<Bicicleta> findByUsario(String texto){
        return repository.findByName(texto);
    }
    @Override
    public Bicicleta persist(Bicicleta bicicleta){
        if (Objects.nonNull(bicicleta)){
            return repository.persist(bicicleta);
        }else {
            return null;
        }
    }

}
