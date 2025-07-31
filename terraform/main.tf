terraform {
  required_providers {
    null = {
      source = "hashicorp/null"
    }
  }
}

resource "null_resource" "simulate_infra" {
  provisioner "local-exec" {
    command = "echo 'Local environment ready: folders, scripts, Jenkins configured manually.'"
  }
}
