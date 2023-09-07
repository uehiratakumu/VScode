module align_module
    implicit none
    contains

    ! 判定関数: 指定された点が既存の球の中にあるか
    logical function is_inside_existing_spheres(point, centers, radius, num_centers)
        integer, intent(in) :: point(3), radius
        integer, intent(in) :: centers(:, :)
        integer, intent(in) :: num_centers
        real :: distance
        integer :: i

        is_inside_existing_spheres = .false.
        do i = 1, num_centers
            distance = sqrt((real(centers(1, i)) - point(1))**2 + (centers(2, i) - point(2))**2 + (centers(3, i) - point(3))**2)
            if (distance < 2 * radius) then
                is_inside_existing_spheres = .true.
                return
            end if
        end do
    end function is_inside_existing_spheres

    ! 立方体の中に最大数の球を配置する関数
    subroutine find_maximum_spheres(cube_size, radius, max_iterations, best_centers, best_count)
        integer, intent(in) :: cube_size, max_iterations
        integer, intent(in) :: radius
        integer, intent(out) :: best_centers(3, 1000) ! 仮に1000としているが、必要に応じて増減させる
        integer, intent(out) :: best_count
        real :: random_point(3), rand_val
        integer :: int_point(3), current_centers(3, 1000)
        integer :: current_count, i, j, max_count
        logical :: inside

        max_count = 0

        ! 10回繰り返して、配置可能な球の数が最大のものを選択
        do i = 1, 10
            current_count = 0
            do j = 1, max_iterations
                ! 立方体の中にランダムに点を配置
                
                call random_number(rand_val)
                random_point(1) = (cube_size - 2*radius)*rand_val + radius
                call random_number(rand_val)
                random_point(2) = (cube_size - 2*radius)*rand_val + radius
                call random_number(rand_val)
                random_point(3) = (cube_size - 2*radius)*rand_val + radius
                int_point =int(random_point)
                inside = is_inside_existing_spheres(int_point, current_centers, radius, current_count)
                ! その点が既存の球の中にない場合、新しい球の中心として追加
                if (.not. inside) then
                    current_count = current_count + 1
                    current_centers(:, current_count) = int_point
                end if
            end do
            if (current_count > max_count) then
                max_count = current_count
                best_centers = current_centers
            end if
        end do
        best_count = max_count
    end subroutine find_maximum_spheres

end module align_module

program align
    use align_module
    real :: best_centers_r(3, 1000)
    integer :: best_count, cube_size, max_iterations,radius,best_centers(3, 1000)

    cube_size = 50
    radius = 8
    max_iterations = 10000

    call find_maximum_spheres(cube_size, radius, max_iterations, best_centers, best_count)
    !print *, "Number of spheres:", best_count
    !print *, "Centers of the spheres:"
    do i=1, best_count
        !print *, best_centers(:, i)
    end do

end program align
