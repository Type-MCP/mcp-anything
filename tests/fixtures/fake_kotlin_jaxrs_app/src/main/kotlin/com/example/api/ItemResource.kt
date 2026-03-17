package com.example.api

import javax.ws.rs.*
import javax.ws.rs.core.MediaType

@Path("/api/items")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
class ItemResource {

    @GET
    fun listItems(@QueryParam("category") category: String?): List<Item> {
        return emptyList()
    }

    @GET
    @Path("/{id}")
    fun getItem(@PathParam("id") id: Long): Item {
        return Item()
    }

    @POST
    fun createItem(@QueryParam("name") name: String): Item {
        return Item()
    }

    @PUT
    @Path("/{id}")
    fun updateItem(@PathParam("id") id: Long, @QueryParam("name") name: String?): Item {
        return Item()
    }

    @DELETE
    @Path("/{id}")
    fun deleteItem(@PathParam("id") id: Long) {
    }
}
