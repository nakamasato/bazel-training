package uuid

import (
	"github.com/google/uuid"
)

func Generate() (string, error) {
	u, err := uuid.NewUUID()
	if err != nil {
		return "", err
	}
	return u.String(), nil
}
