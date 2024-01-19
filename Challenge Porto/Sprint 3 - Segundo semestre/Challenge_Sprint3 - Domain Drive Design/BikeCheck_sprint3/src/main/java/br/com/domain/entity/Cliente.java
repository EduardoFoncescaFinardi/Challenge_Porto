package br.com.domain.entity;

import java.util.ArrayList;
import java.util.List;

public class Cliente {

    private Long id;
    private String usuario;
    private String senha;
    private List<Bicicleta> bicicletas;

    public Cliente() {
        this.bicicletas = new ArrayList<>();
    }

    public Cliente(Long id, String usuario, String senha) {
        this.id = id;
        this.usuario = usuario;
        this.senha = senha;
        this.bicicletas = new ArrayList<>();
    }

    public Long getId() {
        return id;
    }

    public Cliente setId(Long id) {
        this.id = id;
        return this;
    }

    public String getUsuario() {
        return usuario;
    }

    public Cliente setUsuario(String usuario) {
        this.usuario = usuario;
        return this;
    }

    public String getSenha() {
        return senha;
    }

    public Cliente setSenha(String senha) {
        this.senha = senha;
        return this;
    }

    public List<Bicicleta> getBicicletas() {
        return bicicletas;
    }

    public void addBicicleta(String bicicleta) {
        Bicicleta novaBicicleta = new Bicicleta(); // Crie uma nova instância de Bicicleta
        novaBicicleta.set(bicicleta); // Defina o nome da bicicleta com base na String
        this.bicicletas.add(novaBicicleta); // Adicione a nova bicicleta à lista
    }



    @Override
    public String toString() {
        return "Cliente{" +
                "id=" + id +
                ", usuario='" + usuario + '\'' +
                ", senha='" + senha + '\'' +
                ", bicicletas=" + bicicletas +
                '}';
    }
}
