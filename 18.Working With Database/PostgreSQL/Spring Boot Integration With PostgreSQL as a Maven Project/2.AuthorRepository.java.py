""


'''



import org.springframework.data.jpa.repository.JpaRepository; 
import org.springframework.stereotype.Repository; 

import com.gfg.postgresql.model.geek_author; 

@Repository
public interface AuthorRepository extends JpaRepository<geek_author, Long>{ 

}


'''