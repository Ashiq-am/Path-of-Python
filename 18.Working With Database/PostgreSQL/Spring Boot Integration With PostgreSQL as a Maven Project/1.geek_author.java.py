""""""

'''

import javax.persistence.Entity; 
import javax.persistence.GeneratedValue; 
import javax.persistence.GenerationType; 
import javax.persistence.Id; 
import javax.persistence.Table; 

@Entity
@Table(name = "geek_author") 
public class geek_author { 
	@Id
	@GeneratedValue(strategy=GenerationType.SEQUENCE) 
	private Integer author_id; 

	private String author_name; 

	private String email_id; 

	public Integer getAuthor_id() { 
		return author_id; 
	} 

	public void setAuthor_id(Integer author_id) { 
		this.author_id = author_id; 
	} 

	public String getAuthor_name() { 
		return author_name; 
	} 

	public void setAuthor_name(String author_name) { 
		this.author_name = author_name; 
	} 

	public String getEmail_id() { 
		return email_id; 
	} 

	public void setEmail_id(String email_id) { 
		this.email_id = email_id; 
	}	 
	
}


'''