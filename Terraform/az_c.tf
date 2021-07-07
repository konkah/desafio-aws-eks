# availability zone C
data "aws_availability_zone" "desafio_EKS_c" {
  name = "us-east-1c"
}
#
## public subnet C public
#resource "aws_subnet" "desafio_EKS_c_public" {
#  vpc_id            = aws_vpc.desafio_EKS.id
#  cidr_block        = "10.0.1.0/24"
#  availability_zone = data.aws_availability_zone.desafio_EKS_c.name
#
#  tags = var.tags
#}
#
## private subnet C APP
#resource "aws_subnet" "desafio_EKS_c_app" {
#  vpc_id            = aws_vpc.desafio_EKS.id
#  cidr_block        = "10.0.5.0/24"
#  availability_zone = data.aws_availability_zone.desafio_EKS_c.name
#
#  tags = var.tags
#}
#
# private subnet C DB
resource "aws_subnet" "desafio_EKS_c_db" {
  vpc_id            = aws_vpc.desafio_EKS.id
  cidr_block        = "10.0.0.128/25"
  availability_zone = data.aws_availability_zone.desafio_EKS_c.name

  tags = var.tags
}