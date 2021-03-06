resource "aws_vpc" "desafio_EKS" {
  cidr_block           = "10.0.0.0/24"
  enable_dns_hostnames = true

  tags = var.tags
}

##igw
#resource "aws_internet_gateway" "desafio_EKS" {
#  vpc_id = aws_vpc.desafio_EKS.id
#
#  tags = var.tags
#}
#
# nat gateway A
#resource "aws_eip" "desafio_EKS_a" {
#  vpc  = true
#
#  depends_on = [
#    aws_internet_gateway.desafio_EKS
#  ]
#
#  tags = var.tags
#}
#
#resource "aws_nat_gateway" "desafio_EKS_a" {
#  allocation_id = aws_eip.desafio_EKS_a.id
#  subnet_id     = aws_subnet.desafio_EKS_a_public.id
#
#  depends_on = [
#    aws_internet_gateway.desafio_EKS
#  ]
#
#  tags = var.tags
#}
#
## nat gateway C
#resource "aws_eip" "desafio_EKS_c" {
#  vpc  = true
#
#  depends_on = [
#    aws_internet_gateway.desafio_EKS
#  ]
#
#  tags = var.tags
#}
#
#resource "aws_nat_gateway" "desafio_EKS_c" {
#  allocation_id = aws_eip.desafio_EKS_c.id
#  subnet_id     = aws_subnet.desafio_EKS_c_public.id
#
#  depends_on = [
#    aws_internet_gateway.desafio_EKS
#  ]
#
#  tags = var.tags
#}