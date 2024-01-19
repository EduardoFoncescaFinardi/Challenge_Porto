package br.com.domain.service;

import java.util.List;

public interface Service<T, U> {

    public List<T> findAll();

    public T findById(U id);

    public List<T> findByUsario(String texto);

    public T persist(T t);
}
