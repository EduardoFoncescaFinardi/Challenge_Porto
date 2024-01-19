package br.com.domain.repository;

import br.com.domain.entity.Cliente;

import java.util.ArrayList;
import java.util.List;

public class ClienteRepository implements Repository<Cliente, Long>{

    private List<Cliente> clientes;

    public ClienteRepository(){
        clientes = new ArrayList<>();
    }
    @Override
    public List<Cliente> findAll(){
        return clientes;
    }
    @Override
    public Cliente findById(Long id){
        for (Cliente c : clientes){
            if (c.getId().equals(id)){
                return c;
            }
        }
        return null;
    }
    @Override
    public List<Cliente> findByName(String nome){
        List<Cliente> clientesCadastrado = new ArrayList<>();
        for (Cliente c: clientes){
            if (c.getUsuario().equalsIgnoreCase(nome)){
                clientesCadastrado.add(c);
            }
        }
        return clientesCadastrado;
    }

    public List<Cliente> findBySenha(String senha){
        List<Cliente> cpfCadastrado = new ArrayList<>();
        for (Cliente c : clientes){
            if (c.getSenha().equalsIgnoreCase(senha)){
                cpfCadastrado.add(c);
            }
        }
        return cpfCadastrado;
    }
    @Override
    public Cliente persist(Cliente c){
        c.setId(clientes.size() + 1L);
        this.clientes.add(c);
        return c;
    }
}
