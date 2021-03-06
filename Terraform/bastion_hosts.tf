#resource "aws_instance" "desafio_EKS_a" {
#  ami                         = data.aws_ami.bastion.id
#  key_name                    = aws_key_pair.bastion_key.key_name
#  instance_type               = "t2.micro"
#  subnet_id                   = aws_subnet.desafio_EKS_a_public.id
#  security_groups             = [aws_security_group.allow_ssh_bastion.id]
#  associate_public_ip_address = true
#
#  tags = {
#    Name = "desafio_EKS_bastion_a"
#  }
#
#  provisioner "file" {
#    source      = "../Database/produtos.sql"
#    destination = "/tmp/produtos.sql"
#  }
#
#  provisioner "file" {
#    source      = "../Database/clientes.sql"
#    destination = "/tmp/clientes.sql"
#  }
#
#  provisioner "file" {
#    source      = "../Keys/bastion_key"
#    destination = "/tmp/bastion_key"
#  }
#
#  provisioner "remote-exec" {
#    inline = [
#      "sudo apt update",
#      "sudo apt upgrade -y",
#      "sudo apt install -y mysql-client",
#      "mysql -u${aws_db_instance.desafio_EKS_clientes.username} -p${aws_db_instance.desafio_EKS_clientes.password} -h${aws_db_instance.desafio_EKS_clientes.address} < /tmp/clientes.sql",
#      "mysql -u${aws_db_instance.desafio_EKS_produtos.username} -p${aws_db_instance.desafio_EKS_produtos.password} -h${aws_db_instance.desafio_EKS_produtos.address} < /tmp/produtos.sql",
#      "chmod 600 /tmp/bastion_key",
#    ]
#  }
#
#  connection {
#    type        = "ssh"
#    user        = "ubuntu"
#    host        = self.public_ip
#    private_key = file("../Keys/bastion_key")
#  }
#
#  depends_on = [
#    aws_db_instance.desafio_EKS_clientes,
#    aws_db_instance.desafio_EKS_produtos
#  ]
#}
#
#output "bastion_a" {
#  value = aws_instance.desafio_EKS_a.public_ip
#}
#
#resource "aws_instance" "desafio_EKS_c" {
#  ami                         = data.aws_ami.bastion.id
#  key_name                    = aws_key_pair.bastion_key.key_name
#  instance_type               = "t2.micro"
#  subnet_id                   = aws_subnet.desafio_EKS_c_public.id
#  security_groups             = [aws_security_group.allow_ssh_bastion.id]
#  associate_public_ip_address = true
#
#  tags = {
#    Name = "desafio_EKS_bastion_c"
#  }
#}
#
#output "bastion_c" {
#  value = aws_instance.desafio_EKS_c.public_ip
#}
#
#data "aws_ami" "bastion" {
#  most_recent = true
#
#  filter {
#    name   = "name"
#    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
#  }
#
#  filter {
#    name   = "virtualization-type"
#    values = ["hvm"]
#  }
#
#  owners = ["099720109477"] # Canonical
#}
#
#resource "aws_security_group" "allow_ssh_bastion" {
#  description = "Allow SSH Bastion Host"
#  vpc_id      = aws_vpc.desafio_EKS.id
#
#  ingress {
#    description = "SSH Port"
#    from_port   = 22
#    to_port     = 22
#    protocol    = "tcp"
#    cidr_blocks = ["201.82.38.163/32"]
#  }
#
#  egress {
#    from_port   = 0
#    to_port     = 0
#    protocol    = "-1"
#    cidr_blocks = ["0.0.0.0/0"]
#  }
#
#  tags = {
#    Name = "SSH_AWS_bastion"
#  }
#}