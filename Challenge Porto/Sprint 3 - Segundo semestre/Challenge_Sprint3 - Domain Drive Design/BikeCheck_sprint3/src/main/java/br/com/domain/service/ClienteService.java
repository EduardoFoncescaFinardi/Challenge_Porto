package br.com.domain.service;

import br.com.domain.entity.Cliente;
import br.com.domain.repository.ClienteRepository;

import java.util.List;
import java.util.Objects;

public class ClienteService implements Service<Cliente, Long>{

    private ClienteRepository repository;

    public ClienteService(){
        this.repository = new ClienteRepository();
    }
    @Override
    public List<Cliente> findAll(){
        return repository.findAll();
    }
    @Override
    public Cliente findById(Long id){
        return repository.findById(id);
    }
    @Override
    public List<Cliente> findByUsario(String usario){
        return repository.findByName(usario);
    }

    public List<Cliente> findBysenha(String senha){
        return repository.findBySenha(senha);
    }
    @Override
    public Cliente persist(Cliente cliente){
        if (Objects.nonNull(cliente)){
            return repository.persist(cliente);
        }else {
            return null;
        }
    }
}
