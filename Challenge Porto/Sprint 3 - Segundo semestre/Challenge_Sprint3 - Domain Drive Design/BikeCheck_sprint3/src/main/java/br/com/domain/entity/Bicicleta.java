package br.com.domain.entity;


public class Bicicleta {
    private Long id;

    private String modeloBicicleta;

    private String nome;

    public Bicicleta(long l, String modeloBicicleta) {
        this.id = id;
        this.modeloBicicleta = modeloBicicleta;
    }

    public void set(String bicicleta) {
    }

    public Bicicleta() {
    }

    public Bicicleta(Long id, String modeloBicicleta, double preco, String nome) {
        this.id = id;
        this.modeloBicicleta = modeloBicicleta;
        this.nome = nome;
    }


    public Long getId() {
        return id;
    }

    public Bicicleta setId(Long id) {
        this.id = id;
        return this;
    }

    public String getModeloBicicleta() {
        return modeloBicicleta;
    }

    public Bicicleta setModeloBicicleta(String modeloBicicleta) {
        this.modeloBicicleta = modeloBicicleta;
        return this;
    }


    public String getNome() {
        return nome;
    }

    public Bicicleta setNome(String nome) {
        this.nome = nome;
        return this;
    }

    @Override
    public String toString() {
        return "Bicicleta{" +
                "id=" + id +
                ", modeloBicicleta='" + modeloBicicleta + '\'' +
                ", nome='" + nome + '\'' +
                '}';
    }

    public void setPecas(String pecasEscolhidas) {
    }
}



