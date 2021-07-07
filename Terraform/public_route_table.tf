## public route table
#resource "aws_route_table" "desafio_EKS_public" {
#  vpc_id = aws_vpc.desafio_EKS.id
#
#  route {
#    cidr_block = "0.0.0.0/0"
#    gateway_id = aws_internet_gateway.desafio_EKS.id
#  }
#
#  tags = var.tags
#}
#
#resource "aws_route_table_association" "desafio_EKS_public_a" {
#  subnet_id      = aws_subnet.desafio_EKS_a_public.id
#  route_table_id = aws_route_table.desafio_EKS_public.id
#}
#
#resource "aws_route_table_association" "desafio_EKS_public_c" {
#  subnet_id      = aws_subnet.desafio_EKS_c_public.id
#  route_table_id = aws_route_table.desafio_EKS_public.id
#}