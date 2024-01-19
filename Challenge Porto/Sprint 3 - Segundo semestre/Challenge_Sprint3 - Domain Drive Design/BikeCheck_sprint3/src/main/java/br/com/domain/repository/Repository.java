package br.com.domain.repository;


import java.util.List;

public interface Repository<T, U> {

    public List<T> findAll();

    public T findById(U id);

    public List<T> findByName(String nome);


    public T persist(T t);

}