package main

import (
	"github.com/nakamasato/bazel-training/uuid"
	"log"
)

func main() {
	id, err := uuid.Generate()
	if err != nil {
		log.Fatal(err)
	}
	log.Println(id)
}
