package com.example.api;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.util.List;

@Path("/api/items")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ItemResource {

    @GET
    public List<Item> listItems(@QueryParam("category") String category) {
        return List.of();
    }

    @GET
    @Path("/{id}")
    public Item getItem(@PathParam("id") Long id) {
        return new Item();
    }

    @POST
    public Item createItem(@QueryParam("name") String name) {
        return new Item();
    }

    @PUT
    @Path("/{id}")
    public Item updateItem(@PathParam("id") Long id, @QueryParam("name") String name) {
        return new Item();
    }

    @DELETE
    @Path("/{id}")
    public void deleteItem(@PathParam("id") Long id) {
    }
}
