package com.example.api;

import io.micronaut.http.annotation.*;
import java.util.List;

@Controller("/api/orders")
public class OrderController {

    @Get("/")
    public List<Order> listOrders(@QueryValue String status) {
        return List.of();
    }

    @Get("/{id}")
    public Order getOrder(@PathVariable Long id) {
        return new Order();
    }

    @Post("/")
    public Order createOrder(@Body Map<String, Object> data) {
        return new Order();
    }

    @Put("/{id}")
    public Order updateOrder(@PathVariable Long id, @Body Map<String, Object> data) {
        return new Order();
    }

    @Delete("/{id}")
    public void deleteOrder(@PathVariable Long id) {
    }
}
