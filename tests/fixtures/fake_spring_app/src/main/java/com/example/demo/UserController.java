package com.example.demo;

import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping
    public List<User> getAllUsers(@RequestParam(required = false) String role) {
        return List.of();
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return new User();
    }

    @PostMapping
    public User createUser(@RequestBody Map<String, Object> userData) {
        return new User();
    }

    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody Map<String, Object> userData) {
        return new User();
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
    }

    @GetMapping("/search")
    public List<User> searchUsers(
            @RequestParam String query,
            @RequestParam(required = false, defaultValue = "10") Integer limit) {
        return List.of();
    }
}
