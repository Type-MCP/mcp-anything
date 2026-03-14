package com.example.api

import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/users")
class UserController {

    @GetMapping
    fun listUsers(@RequestParam(required = false) role: String?): List<User> {
        return emptyList()
    }

    @GetMapping("/{id}")
    fun getUser(@PathVariable id: Long): User {
        return User()
    }

    @PostMapping
    fun createUser(@RequestBody body: UserRequest): User {
        return User()
    }

    @PutMapping("/{id}")
    fun updateUser(@PathVariable id: Long, @RequestParam name: String): User {
        return User()
    }

    @DeleteMapping("/{id}")
    fun deleteUser(@PathVariable id: Long) {
    }
}
